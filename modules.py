class Activities_map:
    settings = {
        'volume_settings': ['slider', 'popup'],
        'tone': ['treble', 'bass']
    }
    voice = {
        'abc': 'asgdfg'
    }


class Modules:
    data = {
        'settings': Activities_map.settings,
        'voice': Activities_map.voice
    }


def locators_check():
    apps = list(Modules.data.keys())
    for i in apps:
        print("Module = " + i)
        act = getattr(Activities_map, i)
        act_pages = list(act.keys())
        print(f"activity page in {i} = " + act_pages[0])
        for j in list(act.values()):
            print(list(act.values()))
            print(f"locators in {i} at " + j[0])


class test:
    def launch(self):
        pass


locators_check()
