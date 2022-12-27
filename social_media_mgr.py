import gptools.functions as ai
import time

API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
ai.api_login(API_KEY_PATH)





class ContentGenerator:
    def __init__(self, topic, details):
        self.edited = []
        self.drafts = []
        self.topic = topic
        self.details = details
        self.ideas = []

    def generate_ideas(self):
        prompt = f"You are a social media manager. You've been tasked with coming up with a campaign about {self.topic}." \
                 f"You have been given the following details:{self.details}. Brainstorm a numbered list of 10 campaign "\
                 f"ideas. "
        try:
            response = ai.generate_text(prompt)
        except:
            print("GPT-3 failed to generate ideas, server may be overloaded. trying again in 10 sec.")
            time.sleep(10)
            response = ai.generate_text(prompt)
        # split the ideas into a list at each line break
        response = response.split("\n")
        # remove any empty strings from the list
        response = [idea for idea in response if idea != ""]
        for idea in response:
            self.ideas.append(idea)

        return self.ideas

    def draft_content(self):

        for idea in self.ideas:
            prompt = f"Draft the text of an Instagram post for the following campaign idea: \n {idea} \n "
            try:
                response = ai.generate_text(prompt)
            except:
                print("GPT-3 failed to generate drafts, server may be overloaded. trying again in 10 sec.")
                time.sleep(10)
                response = ai.generate_text(prompt)
            self.drafts.append(response)
        return self.drafts

    def edit_content(self):
        for draft in self.drafts:
            try:
                draft = ai.refine_text(draft, "make these Instagram posts more engaging")
            except:
                print("GPT-3 failed to edit drafts, server may be overloaded. trying again in 10 sec.")
                time.sleep(10)
                draft = ai.refine_text(draft, "make these Instagram posts more engaging")
            self.edited.append(draft)
        return self.edited


# class SocialMediaManager:
#     def __init__(self, platforms: List[str]):
#         self.platforms = platforms
#
#     def post_content(self, content: List[str]) -> None:
#         for platform in self.platforms:
#             # Publish the content to the specified platform
#             pass
#
#     def respond_to_comments_and_messages(self, platform: str) -> None:
#         # Respond to comments and messages on the specified platform
#         pass
#
#     def analyze_performance(self, platform: str) -> Dict[str, int]:
#         metrics = {}
#         # Gather and return metrics such as engagement, reach, and conversion rates
#         return metrics
#
#
# class ContentAnalytics:
#     def track_metrics(self, content: List[str], platform: str) -> Dict[str, int]:
#         metrics = {}
#         # Gather and return metrics such as engagement, reach, and conversion rates
#         return metrics
#
#     def generate_reports(self, metrics: Dict[str, int]) -> str:
#         report = ""
#         # Generate and return a formatted report on the performance of the content
#         return report
#
#
# class ClientManager:
#     def __init__(self, clients: List[str]):
#         self.clients = clients
#
#     def onboard_client(self, client: str) -> None:
#         # Onboard the new client
#         pass
#
#     def handle_client_inquiries(self, client: str) -> None:
#         # Handle inquiries and requests from the client
#         pass
#
#     def track_project_status(self, client: str) -> str:
#         status = ""
#         # Track the status of ongoing projects for the client
#         return status


campaign = ContentGenerator("A Grand opening for 'ladybird brewing, a brewery that focuses on farmhouse ales and sour beers",
                            "the grand opening is on May 5th 2023, there will be live music with 'Zaq Squares' the "
                            "flagship beer is 'of the stars - belgian style open fermented sour ale' and the brewery "
                            "is located in the city of 'Asheville NC' on the south slope")
ideas = campaign.generate_ideas()
for idea in ideas:
    print(idea)

drafts = campaign.draft_content()
for draft in drafts:
    print(draft)

edited = campaign.edit_content()
for final in edited:
    print(final)
