import openai
import telebot

# API KEY di openAI
openai.api_key = " "
# API_KEY bot telegram
bot = telebot.TeleBot(" ")

# Richiesta a chatGPT
def genera_risposta_chatgpt3(messaggio):
    # openAi.Completion.create --> permette di generare completamenti automatici di testo utilizzando
    # il modello di linguaggio GPT.
    # Essa prende come parametro un oggetto JSON con
    # alcune informazioni relative alla richiesta di completamento del testo
    risposta = openai.Completion.create(
        model="text-davinci-003",
        prompt=messaggio,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )

    # choices[0] --> sceglie la prima risposta tra le possibili suggerite da chatGPT
    # .text --> le trasforma in testo
    # strip()-->elimina eventuali spazi bianchi
    return risposta.choices[0].text.strip()


# decoratore -->  utilizzato per estendere o aggiungere funzionalità ad una funzione esistente,
# senza doverne modificare il codice sorgente originale
# @bot.message_handler indica che la funzione decorata sarà richiamata
# ogni volta che il bot riceve un nuovo messaggio.
# Il parametro func specifica la funzione che verrà chiamata per determinare
# se la funzione decorata deve essere eseguita o meno, in base alle caratteristiche del messaggio.
# In questo caso, lambda message: True è una funzione lambda che restituisce sempre il valore True,
# il che significa che la funzione decorata verrà sempre eseguita per qualsiasi messaggio ricevuto.
# In sostanza, questo decoratore è un modo per registrare una funzione come handler
# per i messaggi ricevuti dal bot, e la sua esecuzione sarà determinata dalla funzione specificata come parametro func.

@bot.message_handler(func=lambda message: True)
def chat(message):
    res = genera_risposta_chatgpt3(message.text)
    bot.reply_to(message, res)

# avviare il bot
bot.polling()
