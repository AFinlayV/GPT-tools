import gptools as ai

ai.api_login()

premise = "a group of young adults who meet at a dive bar in asheville nc"
genre = "dark comedy"
characters = "Bill: the loveable town drunk, Angie: the plucky bartender, Phill: the gruff maintainence guy, Trevor: the rich bar owner, Frank: the autistic nerdy bar patron, Milton: the new guy in town"
setting = "A Dive Bar in asheville nc"
style = "Single camera scripted comedy"


# make the code below an object called tv_show
class tv_show:
    def __init__(self, premise, genre, characters, setting, style):
        self.episode_script = None
        self.episode_summary = None
        self.episode_summaries = None
        self.premise = premise
        self.genre = genre
        self.characters = characters
        self.setting = setting
        self.style = style
        self.tv_show = None
        self.character_descriptions = None
        self.filename = None
        self.refine_by = None
        self.critique = None

    def generate_tv_show(self):
        prompt = f"generate a tv show with the following details: \n premise:{self.premise} \n genre: {self.genre} \n " \
                 f"characters: {self.characters} \n setting: {self.setting} \n style: {self.style} \n "
        self.tv_show = ai.generate_text(prompt)
        return self.tv_show

    def refine_tv_show(self):
        self.tv_show, self.critique = ai.refine_text(self.tv_show, self.refine_by)
        return self.tv_show

    # a method that generates the pitch for the tv show given the details above
    def generate_pitch(self):
        prompt = f"generate a pitch for the following tv show: \n premise:{self.premise} \n genre: {self.genre} \n " \
                 f"characters: {self.characters} \n setting: {self.setting} \n style: {self.style} \n "
        self.pitch = ai.generate_text(prompt)
        return self.pitch

    # a method that generates the character descriptions for the tv show given the details above
    def generate_character_descriptions(self):
        prompt = f"generate character descriptions for the following tv show: \n premise:{self.premise} \n genre: {self.genre} \n " \
                 f"characters: {self.characters} \n setting: {self.setting} \n style: {self.style} \n pitch: {self.pitch} \n "
        self.character_descriptions = ai.generate_text(prompt)
        return self.character_descriptions

    # a method that generates a list of episodes with short descriptions for the tv show given the details above

    def generate_episode_list(self):
        prompt = f"generate a numbered list of episodes for the following tv show: \n premise:{self.premise} \n genre: {self.genre} \n pitch: {self.pitch} \n characters: {self.characters} \n setting: {self.setting} \n style: {self.style} \n Each episode should be 30 minutes long and start with 'EPISODE #' and then the episode number. \n "
        self.episode_list = ai.generate_text(prompt)
        # split the episodes into a list at each episode number
        self.episode_list = self.episode_list.split("EPISODE")
        # remove any empty strings from the list
        self.episode_list = [episode for episode in self.episode_list if episode != ""]
        print(f"episode list: {self.episode_list}")
        return self.episode_list
    def generate_episode_summaries(self):
        self.episode_summaries = []
        for episode in self.episode_list:
            prompt = f"generate a detailed 3 act summary for the following episode: \n {episode} \n for a tv show with the following details: \npremise:{self.premise} \n genre: {self.genre} \n " \
                     f"characters: {self.characters} \n setting: {self.setting} \n style: {self.style} \n pitch: {self.pitch} \n "
            episode_summary = ai.generate_text(prompt)
            episode_summary = f"{episode} - \n {episode_summary}"
            self.episode_summaries.append(episode_summary)
            print(episode_summary)
        print(self.episode_summaries)
        with open("episode_summaries.txt", "a") as f:
            for episode_summary in self.episode_summaries:
                f.write(episode_summary)
        return self.episode_summaries

    def generate_episode_scripts(self):
        self.episode_scripts = []
        i = 1
        for episode in self.episode_summaries:
            prompt = f"generate a script for the following episode: \n {episode} \n premise:{self.premise} \n genre: {self.genre} \n " \
                     f"characters: {self.characters} \n setting: {self.setting} \n style: {self.style} \n pitch: {self.pitch} \n "
            episode_script = ai.generate_text(prompt)
            self.episode_scripts.append(episode_script)
            title = ai.generate_text(f"generate a title for the following episode: \n {episode} \n premise:{self.premise} \n genre: {self.genre} \n ")
            print(f"{title} - \n {episode_script}")
            with open(f"{i} - {title}.txt", "a") as f:
                f.write(self.episode_script)
            i += 1
        return self.episode_scripts

    def episode_scripts(self):
        pass


# make an object called my_tv_show
my_tv_show = tv_show(premise, genre, characters, setting, style)
# generate the tv show
my_tv_show.generate_tv_show()
print(my_tv_show.tv_show)
# generate the pitch
my_tv_show.generate_pitch()
print(my_tv_show.pitch)
#generate an episode list
my_tv_show.generate_episode_list()
print(my_tv_show.episode_list)
# generate the character descriptions
my_tv_show.generate_character_descriptions()
print(my_tv_show.character_descriptions)
# generate the episode summaries
my_tv_show.generate_episode_summaries()
print(my_tv_show.episode_summaries)
# generate the episode scripts
my_tv_show.generate_episode_scripts()
print(my_tv_show.episode_scripts)




