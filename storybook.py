import os
import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key = os.environ['OPENAI_API_KEY']
)

#Story
def story_gen(prompt):
  system_prompt = """
  You are a world renowned author for young adults fiction short stories.
  Given a concept, generate a short story relevant to the themes of the concept with a twist ending.
  The total length of the story should write within 100 words
  """

  response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=1.3,  # Added a comma here
        max_tokens=2000
    )
  return response.choices[0].message.content 
  # Fixed indentation: Aligned with the function definition


#Cover art
def art_gen(prompt):
  response = client.images.generate(
      prompt=prompt,
      model="dall-e-2",
      n=1,
     quality="hd",
      size="512x512"
  )
  image_url = response.data[0].url
  return image_url

#Cover prompt design
def design_gen(prompt):
  system_prompt = """
  You will be given a short story. Generate a prompt for a cover art that is suitable for the story. The prompt is for dall-e-2
  """
  response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages = [
           {"role": "system", "content": system_prompt},
           {"role": "user", "content": prompt}
      ],
       temperature=1.3,  
       max_tokens=2000
  )
  return response.choices[0].message.content

prompt = st.text_input("Enter a prompt")
if st.button("Generate"):
  story = story_gen(prompt)
  art = art_gen(prompt)
  design = design_gen(prompt)

  st.caption(design)
  st.divider()
  st.write(story)
  st.divider()
  st.image(art)


