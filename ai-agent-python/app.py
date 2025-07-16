import os
import google.generativeai as genai
from PIL import Image

def configure_gemini(api_key):
    """Configure Gemini API with the provided key"""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(model, prompt, image_path=None):
    """Get response from Gemini model"""
    try:
        if image_path:
            # Load and process image
            image = Image.open(image_path)
            # Multi-modal input (text + image)
            response = model.generate_content([prompt, image])
        else:
            # Text-only input
            response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("🤖 Multi-Modal AI Agent with Gemini")
    print("=" * 50)
    
    # Get API key
    api_key = input("Enter your Gemini API key: ")
    
    if not api_key:
        print("API key is required. Get it from: https://makersuite.google.com/app/apikey")
        return
    
    # Configure model
    try:
        model = configure_gemini(api_key)
        print("✅ Gemini model configured successfully!")
    except Exception as e:
        print(f"❌ Error configuring Gemini: {e}")
        return
    
    print("\n" + "=" * 50)
    print("How to use:")
    print("1. Type 'exit' to quit")
    print("2. Type 'image' to analyze an image")
    print("3. Just type your message for text-only chat")
    print("=" * 50)
    
    while True:
        print("\n" + "-" * 30)
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            print("👋 Goodbye!")
            break
        
        elif user_input.lower() == 'image':
            # Image analysis mode
            image_path = input("Enter image file path: ").strip()
            if not os.path.exists(image_path):
                print("❌ Image file not found!")
                continue
            
            question = input("Ask a question about the image: ").strip()
            if not question:
                question = "What do you see in this image?"
            
            print("\n🤖 AI is analyzing the image...")
            response = get_gemini_response(model, question, image_path)
            print(f"AI: {response}")
        
        else:
            # Text-only mode
            if not user_input:
                print("Please enter a message.")
                continue
            
            print("\n🤖 AI is thinking...")
            response = get_gemini_response(model, user_input)
            print(f"AI: {response}")

if __name__ == "__main__":
    main()