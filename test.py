import markovify

with open('test.txt') as f:
    text = f.read()

text_model = markovify.Text(text)

print(text_model.make_short_sentence(700))
