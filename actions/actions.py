import base64
import io
import numpy as np
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

from actions.synthesize_text_action import synthesize_text
import soundfile as sf
import torch
from transformers import pipeline
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from pydub import AudioSegment

class CustomAction(Action):
    def name(self):
        return "custom_action"

    def run(self, dispatcher, tracker, domain):
        text_response = "This is a text response."
        base64_audio = synthesize_text(text_response)

        dispatcher.utter_message(
            text=text_response,
            attachment={
                "type": "audio",
                "payload": {
                    "src": f"data:audio/wav;base64,{base64_audio}"
                }
            }
        )
        return []


class AskMedicalPractice(Action):
    def name(self):
        return "utter_ask_medical_practice"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Cannnn 2 you please tell me the name of your medical practice?")

class AskDoctor(Action):
    def name(self):
        return "utter_ask_doctor"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Can you please tell me the name of your doctor?")

class AskCareCoordinatorName(Action):
    def name(self):
        return "utter_ask_care_coordinator_name"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Do you know the name of your care coordinator?")

class ConfirmCareCoordinatorName(Action):
    def name(self):
        return "utter_confirm_care_coordinator_name"

    def run(self, dispatcher, tracker, domain):
        care_coordinator_name = tracker.get_slot("care_coordinator_name")
        dispatcher.utter_message(f"Great, your care coordinator's name is {care_coordinator_name}.")

class DenyCareCoordinatorName(Action):
    def name(self):
        return "utter_deny_care_coordinator_name"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("I can help locate your Care Coordinator for you.")

class TransferToCareCoordinator(Action):
    def name(self):
        return "utter_transfer_to_care_coordinator"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("I'm going to transfer you to your Care Coordinator now. Please hold for just a moment.")
        # Add code here to transfer the user to the Care Coordinator
        # This could involve making an API call or sending a request to a third-party service

# class SynthesizeTextAction(Action):
#     def name(self):
#         return "synthesize_text"

#     def run(self, dispatcher, tracker, domain):
#         text = tracker.get_slot("text")
#         audio = synthesize_text(text)
#         dispatcher.utter_audio(audio)


class SynthesizeTextAction(Action):
    def name(self):
        return "synthesize_text"
    
    def run(self, dispatcher, tracker, domain):
        text = tracker.latest_message.get("text", "Default response")

        try:
            # Generate the Base64-encoded audio
            base64_audio = synthesize_text(text)

            # Check the output channel
            output_channel = tracker.get_latest_input_channel()

            if output_channel == "cmdline":  # Console output channel
                dispatcher.utter_message("Audio generated successfully, but audio playback is not supported in the console.")
            else:
                # Send the Base64 audio as part of the response for rich media channels
                dispatcher.utter_message(
                    attachment={
                        "type": "audio",
                        "payload": {
                            "src": f"data:audio/wav;base64,{base64_audio}"
                        }
                    }
                )
        except Exception as e:
            dispatcher.utter_message("Sorry, I couldn't generate the audio.")
            print(f"Error generating audio: {e}")

        return []