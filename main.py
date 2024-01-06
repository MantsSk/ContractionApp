from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from datetime import datetime

class ContractionTracker(BoxLayout):
    def __init__(self, **kwargs):
        super(ContractionTracker, self).__init__(**kwargs)
        self.start_time = None
        self.last_end_time = None
        self.contractions = []

    def start_contraction(self):
        self.start_time = datetime.now()
        if self.last_end_time:
            interval = self.start_time - self.last_end_time
            self.ids.interval_label.text = f"Time since last contraction: {interval}"
        else:
            self.ids.interval_label.text = "This is the first contraction."
        self.ids.info_label.text = "Contraction started. Press 'Stop' when it ends."
        self.ids.start_button.disabled = True
        self.ids.stop_button.disabled = False

    def stop_contraction(self):
        end_time = datetime.now()
        duration = end_time - self.start_time
        self.last_end_time = end_time
        self.contractions.append((self.start_time, end_time, duration))
        self.start_time = None
        self.ids.info_label.text = "Press 'Start' for the next contraction."
        self.ids.start_button.disabled = False
        self.ids.stop_button.disabled = True
        self.update_contractions_list()

    def update_contractions_list(self):
        self.ids.contractions_list.clear_widgets()
        for start, end, duration in self.contractions:
            label_text = f"Start: {start.strftime('%Y-%m-%d %H:%M:%S')}, " \
                         f"End: {end.strftime('%Y-%m-%d %H:%M:%S')}, " \
                         f"Duration: {duration}"
            label = MDLabel(text=label_text, size_hint_y=None, height=40)
            self.ids.contractions_list.add_widget(label)

class ContractionTrackerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'  # Set primary color for the app
        return ContractionTracker()

if __name__ == '__main__':
    ContractionTrackerApp().run()
