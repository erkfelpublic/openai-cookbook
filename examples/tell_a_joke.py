import pyjokes
import openai

def tell_a_joke():
  """Prints a random joke from pyjokes."""
  print(pyjokes.get_joke())

def tell_joke(prompt="Tell me a joke"):
  """
  Generates a joke using openai.ChatCompletion.create() and prints it to the console.
  """
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": prompt},
      ],
  )
  print(response.choices[0].message.content)


if __name__ == "__main__":
  tell_a_joke()
  tell_joke("Tell me a joke about a programmer.")
