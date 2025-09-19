
def log(context, message):
    # Guardar el mensaje en el contexto usando el ID del step actual
    if hasattr(context, 'current_step_id') and context.current_step_id:
        if context.current_step_id not in context.step_logs:
            context.step_logs[context.current_step_id] = []
        context.step_logs[context.current_step_id].append(message)
    # También imprimir para debug inmediato
    print(message)