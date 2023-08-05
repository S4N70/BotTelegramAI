# BOT TELEGRAM CHE GENERA FRASI ROMANTICHE ATTRAVERSO L'AI
import openai
import telebot

TOKEN = '6412566892:AAGgacB06EWp5OTQiBuv1MlcIMcqaEXqaTI'
bot = telebot.TeleBot(TOKEN)

openai.api_key = "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"
model_engine = "text-davinci-003"


def genera_frase():
    prompt = "Scrivi una frase poetica legata all'amore "
    try:
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text
    except Exception as e:
        print("Errore durante la generazione della frase:", e)
        return "Si è verificato un errore nella generazione della frase."
    # In questo caso restituirà obbligatoriamente l'errore poichè il token non dispone di un piano a pagamento attivo


testo = genera_frase()
print(testo)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message,
                 f"Ciao, benvenuto io sono un bot molto romantico \n"
                 "digita o premi su /GeneraFrase e io ti creerò una frase romantica")


@bot.message_handler(commands=['GeneraFrase'])
def handle_GeneraFrase(message):
    bot.reply_to(message,
                 "spero la frase sia di tuo gradimento, altrimenti puoi generarne senza problemi un'altra""")


bot.polling()
