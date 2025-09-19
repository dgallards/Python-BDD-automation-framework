import sys
import json
import os
import uuid  # Add this at the top

def before_all(context):
    # Inicializar un diccionario para almacenar logs por step
    context.step_logs = {}
    context.current_step_id = None

def before_scenario(context, scenario):
    """Hook que se ejecuta antes de cada scenario"""
    context.current_scenario_name = scenario.name

def before_step(context, step):
    """Hook que se ejecuta antes de cada step"""
    # Convertir la ubicación del step a string
    base_location = str(step.location) if hasattr(step, 'location') and step.location else f"{step.filename}:{step.line}"
    
    # Combinar scenario name + step location para crear ID único
    scenario_name = getattr(context, 'current_scenario_name', 'unknown')
    context.current_step_id = f"{scenario_name}::{base_location}"

def after_step(context, step):
    # Los logs ya fueron guardados en context.step_logs durante la ejecución
    pass

def after_all(context):
    # Guardar los logs en un archivo JSON separado
    logs_file = 'step_logs.json'
    try:
        with open(logs_file, 'w') as f:
            json.dump(context.step_logs, f, indent=2)
        print(f"Step logs saved to {logs_file}")
    except Exception as e:
        print(f"Error saving step logs: {e}")