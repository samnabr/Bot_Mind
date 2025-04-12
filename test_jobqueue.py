from telegram.ext import Application, JobQueue
from datetime import datetime

# Função de teste
async def callback(context):
    print("Callback executado!")

# Criar a aplicação
app = Application.builder().token('7984935357:AAF1i8h6Q3nBaA97tsd1tsRX-LtpxKkKEhw').build()

# Testar o JobQueue com o parâmetro timezone
job_queue = JobQueue()
job_queue.set_application(app)
job_queue.run_daily(
    callback,
    time=datetime.strptime("08:00", "%H:%M").time(),
    days=(0, 1, 2, 3, 4, 5, 6),
    name="test_job",
    timezone="America/Sao_Paulo"
)

print("Teste concluído com sucesso!")