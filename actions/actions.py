# # from rasa_sdk import Action
# # from rasa_sdk.events import SlotSet
# # from rasa_sdk.interfaces import Tracker
# # from rasa_sdk.executor import CollectingDispatcher

# # import logging

# # # Configure logging
# # logging.basicConfig(level=logging.INFO)


# # class AskMedicalPractice(Action):
# #     def name(self):
# #         return "utter_ask_medical_practice"

# #     def run(self, dispatcher, tracker, domain):
# #         dispatcher.utter_message("Can you please tell me the name of your medical practice?")
# #         logging.info(f"Current slot values: {tracker.slots}")
# #         print(f"Current slot values: {tracker.slots}")

# # class AskDoctor(Action):
# #     def name(self):
# #         return "utter_ask_doctor"

# #     def run(self, dispatcher, tracker, domain):
# #         dispatcher.utter_message("Can you please tell me the name of your doctor?")
# #         logging.info(f"Current slot values: {tracker.slots}")
# #         print(f"Current slot values: {tracker.slots}")

# # class AskCareCoordinatorName(Action):
# #     def name(self):
# #         return "utter_ask_care_coordinator_name"

# #     def run(self, dispatcher, tracker, domain):
# #         dispatcher.utter_message("Do you know the name of your care coordinator?")
# #         logging.info(f"Current slot values: {tracker.slots}")
# #         print(f"Current slot values: {tracker.slots}")

# # class ConfirmCareCoordinatorStartTask(Action):
# #     def name(self):
# #         return "utter_confirm_care_coordinator_start_task"

# #     def run(self, dispatcher, tracker, domain):

# #         dispatcher.utter_message(f"Hello, this is your Care Partner at CoachCare! Thank you for calling. Would you like help getting connected to your Care Coordinator?")
# #         logging.info(f"Current slot values: {tracker.slots}")
# #         print(f"Current slot values: {tracker.slots}")


# # class ConfirmCareCoordinatorName(Action):
# #     def name(self):
# #         return "utter_confirm_care_coordinator_name"

# #     def run(self, dispatcher, tracker, domain):
# #         care_coordinator_name = tracker.get_slot("care_coordinator_name")
# #         dispatcher.utter_message(f"Great, your care coordinator's name is {care_coordinator_name}.")
# #         logging.info(f"Current slot values: {tracker.slots}")
# #         print(f"Current slot values: {tracker.slots}")

# # class DenyCareCoordinatorName(Action):
# #     def name(self):
# #         return "utter_deny_care_coordinator_name"

# #     def run(self, dispatcher, tracker, domain):
# #         dispatcher.utter_message("I can help locate your Care Coordinator for you.")
# #         logging.info(f"Current slot values: {tracker.slots}")
# #         print(f"Current slot values: {tracker.slots}")


# # class ActionHandleGreeting(Action):
# #     def name(self):
# #         return "utter_greet"

# #     def run(self, dispatcher, tracker, domain):
# #         dispatcher.utter_message(
# #             text="Hello, this is your Care Partner at CoachCare! Thank you for calling. Would you like help getting connected to your Care Coordinator?"
# #         )
# #         logging.info(f"Current slot values: {tracker.slots}")
# #         print(f"Current slot values: {tracker.slots}")
# #         return []

# # class TransferToCareCoordinator(Action):
# #     def name(self):
# #         return "utter_transfer_to_care_coordinator"

# #     def run(self, dispatcher, tracker, domain):
# #         dispatcher.utter_message("I'm going to transfer you to your Care Coordinator now. Please hold for just a moment.")
# #         logging.info(f"Current slot values: {tracker.slots}")
# #         print(f"Current slot values: {tracker.slots}")
# #         # Add code here to transfer the user to the Care Coordinator
# #         # This could involve making an API call or sending a request to a third-party service
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet, LoopInterrupted, AllSlotsReset, Form
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import Form, SlotSet
# from rasa_sdk.forms import FormValidationAction

# class CareCoordinatorForm(Action):
#     def name(self) -> Text:
#         return "care_coordinator_form"

#     def run(
#         self, 
#         dispatcher: CollectingDispatcher, 
#         tracker: Tracker, 
#         domain: Dict[Text, Any]
#     ) -> List[Dict]:
#         required_slots = ["clinic_name", "doctor_name", "care_coordinator_name"]

#         for slot in required_slots:
#             if tracker.get_slot(slot) is None:
#                 return [SlotSet("requested_slot", slot)]

#         return [Form(None)]

#     def required_slots(self, tracker: Tracker) -> List[Text]:
#         return ["clinic_name", "doctor_name", "care_coordinator_name"]

#     def submit(
#         self, 
#         dispatcher: CollectingDispatcher, 
#         tracker: Tracker, 
#         domain: Dict[Text, Any]
#     ) -> List[Dict]:
#         dispatcher.utter_message(
#             text=f"Great! I've collected the following information:\n"
#                  f"Clinic: {tracker.get_slot('clinic_name')}\n"
#                  f"Doctor: {tracker.get_slot('doctor_name')}\n"
#                  f"Care Coordinator: {tracker.get_slot('care_coordinator_name')}"
#         )
#         return []
    
# class ValidateCareCoordinatorForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_care_coordinator_form"

#     def validate_clinic_name(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         if isinstance(slot_value, str):
#             return {"clinic_name": slot_value}
#         else:
#             dispatcher.utter_message(text="Please provide a valid clinic name.")
#             return {"clinic_name": None}

#     def validate_doctor_name(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         if isinstance(slot_value, str):
#             return {"doctor_name": slot_value}
#         else:
#             dispatcher.utter_message(text="Please provide a valid doctor name.")
#             return {"doctor_name": None}

#     def validate_care_coordinator_name(
#         self,
#         slot_value: Any,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         if isinstance(slot_value, str):
#             return {"care_coordinator_name": slot_value}
#         else:
#             dispatcher.utter_message(text="Please provide a valid care coordinator name.")
#             return {"care_coordinator_name": None}


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionLookupCoordinatorInfo(Action):
    def name(self) -> Text:
        return "action_lookup_coordinator_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Collect slot values
        practice = tracker.get_slot('medical_practice')
        doctor = tracker.get_slot('doctor_name')
        coordinator = tracker.get_slot('coordinator_name')

        # Simulated lookup result
        dispatcher.utter_message(text=f"Here is the information I found:")
        dispatcher.utter_message(text=f"Name: {coordinator or 'John Doe'}")
        dispatcher.utter_message(text=f"Address: 123 Main Street")
        dispatcher.utter_message(text=f"Phone: 555-123-4567")
        
        dispatcher.utter_message(text="Would you like to be transferred?")
        return []
