from chatterbot import ChatBot

time_positive = ['what is the time right now', 'time', 'clock', 'what is the current time', 'what is the time now',
                 'what’s the time', 'what time is it',
                 'what time is it now', 'do you know what time it is', 'could you tell me the time, please',
                 'what is the time', 'will you tell me the time',
                 'tell me the time', 'time please', 'show me the time', 'what is time', 'whats on the clock',
                 'show me the clock',
                 'what is the time', 'what is on the clock', 'tell me time', 'time', 'clock', 'tell me time',
                 'what is the time',
                 'tell me the time', 'time please', 'show me the time', 'what is time', 'whats on the clock',
                 'show me the clock',
                 ]

time_negative = ['what are you doing', 'what’s up', 'when is time', 'who is time' 'could you', 'do you', 'what’s',
                 'will you', 'tell me', 'show me', 'current', 'do', 'now',
                 'will', 'show', 'tell', 'me', 'could', 'what', 'whats', 'i have time', 'who', 'who is', 'hardtime',
                 'when', 'what is', 'how',
                 'how is', 'when is', 'who is time', 'how is time', 'how is time', 'when is time', 'tell me weather',
                 'weather', 'current weather', 'can you tell me about wine', 'what about wine', 'what wine is this',
                 'wine', 'wine brand',
                 'King Street Brewing Co', 'Brewing', 'Avondale Brewing Co', 'BJs Restaurant & Brewery - Chandler',
                 'Trim Tab Brewing', 'Help me!', 'can you help me!', 'how can you help me']

# Create a new instance of a ChatBot with name Chatbot_Example.
bot = ChatBot('Chatbot_Example',
              database_uri='sqlite:///database.db',
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'Sorry, I am not aware of this.',
                      'maximum_similarity_threshold': 0.9,
                  },
                  {
                      'import_path': 'chatterbot.logic.TimeLogicAdapter',
                      'positive': time_positive,
                      'negative': time_negative

                  },

                  {
                      'import_path': 'chatterbot.logic.MathematicalEvaluation',

                  },

                  {
                      'import_path': 'wine_adapter.wine_logic_adapter.WineLogicAdapter',

                  },
                  {
                      'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                      'input_text': ['Help me!', 'tell me about wine', 'what about wine', 'can you tell me about wine'],
                      'output_text': 'Give me wine name'
                  }

              ],

              )
