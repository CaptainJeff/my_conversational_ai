from rasa.core.channels.channel import OutputChannel

from actions.synthesize_text_action import synthesize_text


# import base64
# from rasa.core.channels.channel import Channel
# from rasa.core.channels.channel import UserMessage

# class CustomAudioChannel(Channel):
#     def __init__(self, audio_synthesizer):
#         self.audio_synthesizer = audio_synthesizer

#     def send_response(self, message):
#         # Synthesize text to audio
#         base64_audio = self.audio_synthesizer.synthesize_text(message.text)

#         # Modify the response payload to include audio attachment
#         message["attachment"] = {
#             "type": "audio",
#             "payload": {
#                 "src": f"data:audio/wav;base64,{base64_audio}"
#             }
#         }

#         # Call the parent class's send_response method
#         super().send_response(message)

from rasa.core.channels.channel import OutputChannel, CollectingOutputChannel

class CustomAudioChannel(OutputChannel):
    @classmethod
    def name(cls) -> str:
        super().__init__()
        # return "custom_audio_channel"
        return "custom_audio_channel"
    # def name(cls) -> str:
    #     
    
    # async def send_text_message(self, recipient_id, text):
    #     # Implement your custom logic to send text messages
    #     print("SENDING TEXT MESSAGE")
    #     pass

    async def send_response(self, recipient_id: str, message: dict):
        print("SENDING RESPONSE")
        # Modify the response to include audio, etc.
        message["attachment"] = {
            "type": "audio",
            "payload": {
                "src": "data:audio/wav;base64,..."
            }
        }
        # Send the modified message
        super().send_response(self, recipient_id, message)

    # async def send_custom_json(self, recipient_id: str, message: dict):
    #     print("SENDING RESPONSE")
    #     # Modify the response to include audio, etc.
    #     message["attachment"] = {
    #         "type": "audio",
    #         "payload": {
    #             "src": "data:audio/wav;base64,..."
    #         }
    #     }
    #     # Send the modified message
    #     super().send_custom_json(self, recipient_id, {
    #         "type": "audio",
    #         "payload": {
    #             "src": "data:audio/wav;base64,..."
    #         }
    #     })








        # await CollectingOutputChannel.send_response(self, recipient_id, message)
