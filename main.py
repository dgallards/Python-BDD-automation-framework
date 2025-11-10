import os
from behave import __main__ as behave_exe
import settings.reportGenerator as reportGenerator

def run_behave():
    # Change to project root so behave can find steps correctly
    os.chdir(os.path.dirname(__file__))  # assumes runner.py is in project root

    # Limpiar archivos de logs anteriores
    for file in ['report.json', 'step_logs.json']:
        if os.path.exists(file):
            os.remove(file)
            print(f"Removed previous {file}")

    tests = ['apis']  # Lista de etiquetas de pruebas a ejecutar

    if tests:
        tags = ' or '.join([f'@{test}' for test in tests])
        print(f'Running tests with tags: {tags}')
        behave_exe.main([
            'tests/features',
            '-t', tags,
            '-f', 'json',
            '-o', 'report.json'
        ])
        
        # Verificar que ambos archivos existan antes de generar el reporte
        if os.path.exists('report.json'):
            report = reportGenerator.ReportGenerator('report.json', 'reports/')
            report.generate_html_report()
        else:
            print("Error: report.json was not generated")
            
    else:
        print("error: No tags provided. Please provide tags to run the tests.")

if __name__ == '__main__':
    run_behave()