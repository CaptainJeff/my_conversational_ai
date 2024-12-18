from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Dict, List, Text
from rasa_sdk.executor import CollectingDispatcher
import logging
from rasa_sdk.events import SlotSet

logger = logging.getLogger(__name__)


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

class ConfirmCareCoordinatorName(Action):
    def name(self):
        return "utter_provide_care_coordinator_name"

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

class ActionProcessCareCoordinatorName(Action):
    def name(self) -> str:
        return "action_process_care_coordinator_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        # Retrieve the care coordinator's name from the slot
        care_coordinator_name = tracker.get_slot("care_coordinator_name")
        print("ActionProcessCareCoordinatorName")
   
        print("tracker", tracker.latest_message)
        print("applied_events", tracker.applied_events())
        print("latest_action_name", tracker.latest_action_name)
        print("get_intent_of_latest_message", tracker.get_intent_of_latest_message())
        print("domain", domain.get("entities"))
        # Example: Custom logic 
        if care_coordinator_name:
            dispatcher.utter_message(
                text=f"Thank you! I’ve noted the care coordinator's name as {care_coordinator_name}. Would you like me to connect you to your care coordinator now?"
            )
        else:
            dispatcher.utter_message(
                text="I couldn't understand the care coordinator's name. Could you please repeat it?"
            )

        logger.info(f"Slot values: {tracker.slots}")


        return []
    
class ActionProcessDoctorName(Action):
    def name(self) -> str:
        return "action_process_doctor_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        # Retrieve the care coordinator's name from the slot
        doctor_name = tracker.get_slot("doctor_name")
        print("ActionProcessCareCoordinatorName")
   
        print("tracker", tracker.latest_message)
        print("domain", domain.get("entities"))
        # Example: Custom logic 
        if doctor_name:
            dispatcher.utter_message(
                text=f"Great. {doctor_name}."
            )
        else:
            dispatcher.utter_message(
                text="I'm sorry. Could you please repeat that?"
            )

        logger.info(f"Slot values: {tracker.slots}")


        return []
    
class ValidateMedicalPracticeAction(Action):
    def name(self) -> Text:
        return "action_validate_medical_practice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        medical_practice = tracker.get_slot("medical_practice")
        print("VALIDATE MEDICAL PRACTICE")
        logger.info(f"VALIDATE MEDICAL PRACTICE")
        print("tracker", tracker.latest_message)
        print("domain", domain.get("entities"))
        
        if not medical_practice:
            dispatcher.utter_message(text="I couldn't understand the name of your medical practice. Could you repeat it?")
            return [SlotSet("medical_practice", None)]
        
        logger.info(f"Slot values: {tracker.slots}")
        return [SlotSet("medical_practice", medical_practice)]