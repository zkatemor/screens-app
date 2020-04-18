import tkinter as tk
import datetime as dt
import app.dropbox_tool as drbx


class CountdownLabel(tk.Label):
    def __init__(self, master, seconds_left):
        super().__init__(master)
        self._seconds_left = seconds_left
        self.seconds = seconds_left
        self._timer_on = False
        self._countdown()  # Start counting down immediately
        self.config(font=("Courier", 44))

    def _start_countdown(self):
        self._stop_countdown()
        self._countdown()

    def _stop_countdown(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def _countdown(self):
        if self._seconds_left:
            self['text'] = self._get_timedelta_from_seconds(self._seconds_left)
            self._seconds_left -= 1
            self._timer_on = self.after(1000, self._countdown)
        elif self._seconds_left == 0:
            self._seconds_left -= 1
            self._timer_on = self.after(1000, self._countdown)
            self._seconds_left = self.seconds
            drbx.take_screenshot()

    @staticmethod
    def _get_timedelta_from_seconds(seconds):
        return dt.timedelta(seconds=seconds)
