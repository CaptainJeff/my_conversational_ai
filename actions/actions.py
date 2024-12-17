from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class AskMedicalPractice(Action):
    def name(self):
        return "utter_ask_medical_practice"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Can you please tell me the name of your medical practice?")

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

class ConfirmCareCoordinatorStartTask(Action):
    def name(self):
        return "utter_confirm_care_coordinator_start_task"

    def run(self, dispatcher, tracker, domain):

        dispatcher.utter_message(f"Hello, this is your Care Partner at CoachCare! Thank you for calling. Would you like help getting connected to your Care Coordinator?")


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


class ActionHandleGreeting(Action):
    def name(self):
        return "utter_greet"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(
            text="Hello, this is your Care Partner at CoachCare! Thank you for calling. Would you like help getting connected to your Care Coordinator?"
        )
        return []

class TransferToCareCoordinator(Action):
    def name(self):
        return "utter_transfer_to_care_coordinator"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("I'm going to transfer you to your Care Coordinator now. Please hold for just a moment.")
        # Add code here to transfer the user to the Care Coordinator
        # This could involve making an API call or sending a request to a third-party service