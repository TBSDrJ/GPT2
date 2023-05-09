from transformers import pipeline, Conversation, GPT2Tokenizer

gen = pipeline('text-generation', model='gpt2-xl')
seq = gen('My name is Marcus Aurelius and I am working on a new concept for a world map.\n\n\nI had thought of a few different designs, but ', max_length=1000, num_return_sequences=1)
for entry in seq:
    print("\n")
    print(entry['generated_text'])
    print("\n\n==========\n\n")

# pipeline = pipeline('conversational', model='gpt2-xl')
# conversation = Conversation()
# while True:
#     new_text = input("Add input: ")
#     conversation.add_user_input(new_text)
#     conversation = pipeline(conversation)
#     print("\n\n> ", end="")
#     print(conversation.generated_responses[-1])
#     print()