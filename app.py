import gradio as gr
from emotion_to_playlist_generator import ai_chatbot  # Rename chatbot.py to ai_chatbot.py if needed

with gr.Blocks(title="Musical Vibe Assistant") as demo:
    gr.HTML(
        "<div style='text-align: center; margin-bottom: 20px;'>"
        "<h1>🎵 Musical Vibe Assistant</h1>"
        "<p>Describe your mood or a scene — get a playlist vibe in return!</p>"
        "</div>"
    )

    gr.ChatInterface(
        fn=ai_chatbot,
        title="🎧 Vibe to Playlist",
        description="Type your mood, emotion, or scene — and get 5 songs that match the vibe.",
        examples=[
            ["I’m heartbroken after a breakup", []],
            ["I feel like dancing in the rain", []],
            ["Nostalgic and missing home", []],
            ["Studying late night and need chill vibes", []],
            ["Feeling like a main character walking through a city at night", []],
        ]
    )

if __name__ == "__main__":
    demo.launch()
