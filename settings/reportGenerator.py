import json
import os
from jinja2 import Template

class ReportGenerator:
    def __init__(self, json_report_path, html_report_path):
        self.json_report_path = json_report_path
        self.html_report_path = html_report_path
        self.step_logs = self.load_step_logs()

    def load_step_logs(self):
        """Cargar logs de steps desde el archivo JSON"""
        try:
            with open('step_logs.json', 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Warning: step_logs.json not found or invalid, proceeding without custom logs")
            return {}

    def get_step_logs(self, step_location, scenario_name=None):
        """Obtener logs para un step específico"""
        
        # Si tenemos el nombre del scenario, buscar con el ID completo
        if scenario_name:
            full_step_id = f"{scenario_name}::{step_location}"
            if full_step_id in self.step_logs:
                return "\n".join(self.step_logs[full_step_id]) if self.step_logs[full_step_id] else ""
        
        # Buscar por ubicación parcial como fallback
        for step_id, logs in self.step_logs.items():
            if step_location in step_id:
                return "\n".join(logs) if logs else ""
        
        return ""

    def sanitize_filename(self, name):
        return "".join(c for c in name if c.isalnum() or c in (' ', '-', '_')).rstrip().replace(" ", "_")

    def extract_logs_from_output(self, output_list):
        """Extrae logs del array de output de Behave"""
        if not output_list:
            return ""
        
        logs = []
        for item in output_list:
            # El output puede venir como string o como dict
            if isinstance(item, str):
                logs.append(item)
            elif isinstance(item, dict):
                # Buscar en diferentes campos donde pueden estar los logs
                if 'text' in item:
                    logs.append(item['text'])
                elif 'message' in item:
                    logs.append(item['message'])
                else:
                    # Si es un dict sin campos conocidos, convertir a string
                    logs.append(str(item))
        
        return "\n".join(logs).strip()

    def generate_html_report(self):
        try:
            with open(self.json_report_path, 'r') as json_file:
                data = json.load(json_file)

            with open('settings/report_templates/global_report_template.html', 'r') as template_file:
                global_template = Template(template_file.read())

            with open('settings/report_templates/feature_report_template.html', 'r') as feature_file:
                feature_template = Template(feature_file.read())

            features = []
            for feature in data:
                status = feature.get('status', 'unknown')
                if status != 'skipped':
                    name = feature.get('name', 'UnnamedFeature')
                    safe_name = self.sanitize_filename(name)
                    features.append({'name': name, 'status': status, 'file': f"{safe_name}.html"})

            rendered_html = global_template.render(features=features)

            for feature in data:
                status = feature.get('status', 'unknown')
                if status != 'skipped':
                    feature_data = {
                        'name': feature.get('name', 'UnnamedFeature'),
                        'status': status,
                        'scenarios': []
                    }
                    for element in feature.get('elements', []):
                        if element['type'] != 'scenario':
                            continue
                        steps = []
                        for step in element.get('steps', []):
                            result = step.get('result', {})
                            step_status = result.get('status', 'unknown')
                            error_message = result.get('error_message', '')
                            
                            # Extraer logs del output de Behave
                            output = result.get('output', [])
                            behave_logs = self.extract_logs_from_output(output)
                            
                            # Obtener logs personalizados de nuestro sistema
                            step_location = step.get('location', '')
                            scenario_name = element.get('name', 'UnnamedScenario')  # Get from the current scenario
                            custom_logs = self.get_step_logs(step_location, scenario_name) 
                            
                            # Combinar todos los logs
                            all_logs = []
                            if custom_logs:
                                all_logs.append(custom_logs)
                            if behave_logs:
                                all_logs.append(behave_logs)
                            
                            # Si no hay logs en output, intentar obtenerlos de otros lugares
                            if not all_logs:
                                # Buscar en el step mismo si tiene información adicional
                                step_output = step.get('output', [])
                                additional_logs = self.extract_logs_from_output(step_output)
                                if additional_logs:
                                    all_logs.append(additional_logs)
                            
                            # Si aún no hay logs, buscar en embedded
                            if not all_logs and 'embedded' in step:
                                for embedded in step['embedded']:
                                    if embedded.get('mime_type') == 'text/plain':
                                        all_logs.append(embedded.get('data', ''))
                            
                            final_logs = "\n".join(all_logs).strip()
                            
                            step_data = {
                                'name': step.get('name', 'Unnamed Step'),
                                'status': step_status,
                                'logs': final_logs,
                                'error': error_message
                            }
                            steps.append(step_data)

                        scenario_status = element.get('status', 'unknown')
                        feature_data['scenarios'].append({
                            'name': element.get('name', 'UnnamedScenario'),
                            'status': scenario_status,
                            'steps': steps
                        })

                    safe_filename = self.sanitize_filename(feature_data['name'])
                    feature_html = feature_template.render(feature=feature_data)
                    feature_file_path = f"reports/{safe_filename}.html"
                    with open(feature_file_path, 'w') as f:
                        f.write(feature_html)

            with open(self.html_report_path + "global.html", 'w') as f:
                f.write(rendered_html)

            print(f"HTML report generated at {self.html_report_path}")

        except Exception as e:
            print(f"Error generating HTML report: {e}")