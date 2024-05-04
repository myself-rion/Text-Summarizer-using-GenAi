import google.generativeai as genai

def text_summarizer(text_to_summarize):
    
    # Configure your API key
    genai.configure(api_key="YOUR_API_KEY")

    # Create a generative model object
    model = genai.GenerativeModel("gemini-1.0-pro-latest")

    # Craft a prompt instructing the model on summarizing text
    prompt = "Summarize this article for me: " + text_to_summarize

    # Generate the text using the prompt and model
    response = model.generate_content(prompt)

    # Access the generated text
    summary_text = response.text

    return summary_text



your_text= input("Please enter the text you want to summarize: ")

summarized_text= text_summarizer(your_text)

print("\nThis is your summarized text: \n", summarized_text)

print(f"\nReduced {len(your_text)-len(summarized_text)} number of words :)")


