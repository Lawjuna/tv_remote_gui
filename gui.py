from tkinter import *
import csv
from moduel import *
global tv_1
tv_1 = Television()
class Gui():
    def __init__(self,window)->None:
        """
        establishes all the buttons and text for the remote
        """

        self.window=window
        self.frame_three = Frame(self.window)
        self.power_button = Button(self.frame_three, text="Power", command=self.power_up)
        self.power_button.pack()
        self.power_shown= Label(self.frame_three,text="off")
        self.power_shown.pack()
        self.frame_three.pack(anchor='w')


        self.frame_one=Frame(self.window,)
        self.channel = Label(self.frame_one, text=' Channel 0')
        self.channel.pack()
        self.frame_one.pack(anchor="center")

        self.frame_two=Frame(self.window)
        self.channel_name= Label(self.frame_two,text='NONE')
        self.channel_name.pack()
        self.frame_two.pack(anchor='center')

        self.frame_seven = Frame(self.window, )
        self.volume = Label(self.frame_seven, text=' Volume')
        self.volume.pack()
        self.volume_shown= Label(self.frame_seven, text='0')
        self.volume_shown.pack()
        self.frame_seven.pack(anchor="center")

        self.frame_four=Frame(self.window)
        self.channel_up_button=Button(self.frame_four,text="Channel UP",width=10,height=5,command=self.channelup)
        self.channel_up_button.pack(side="left")
        self.channel_down_button = Button(self.frame_four, text="Channel Down",width=10,height=5,command=self.channeldown)
        self.channel_down_button.pack(side="left",padx=5)
        self.frame_four.pack(anchor='center',pady=10)

        self.frame_five = Frame(self.window)
        self.volume_up_button = Button(self.frame_five, text="Volume UP", width=10, height=5,command=self.volumeup)
        self.volume_up_button.pack(side="left")
        self.volume_down_button = Button(self.frame_five, text="Volume Down", width=10, height=5,command=self.volumedown)
        self.volume_down_button.pack(side="left", padx=5)
        self.frame_five.pack(anchor='center', pady=10)

        self.frame_six=Frame(self.window)
        self.mute_button = Button(self.frame_six, text="MUTE", width=10, height=3,command=self.mute)
        self.mute_button.pack(side="left")
        self.mute_shown= Label(self.frame_six, text='UNMUTED')
        self.mute_shown.pack()
        self.frame_six.pack(anchor='center')


    def power_up(self)->None:
        """
        Turns the power on or off
        """
        if tv_1.get_status() == False:
            tv_1.power()
            self.power_shown.config(text="on")
        elif tv_1.get_status() == True:
            tv_1.power()
            self.power_shown.config(text="off")
    def volumeup(self)->None:
        """
        turns the volume up
        """
        tv_1.volume_up()
        volume=tv_1.get_volume()
        self.mute_shown.config(text="UNMUTED")
        if volume == 0:
            self.volume_shown.config(text="0")
        elif volume == 1:
            self.volume_shown.config(text="1")
        elif volume == 2:
            self.volume_shown.config(text="2")
        elif volume == 3:
            self.volume_shown.config(text="3")
        elif volume == 4:
            self.volume_shown.config(text="4")
        elif volume == 5:
            self.volume_shown.config(text="5")
        elif volume == 6:
            self.volume_shown.config(text="6")
        elif volume == 7:
            self.volume_shown.config(text="7")
        elif volume == 8:
            self.volume_shown.config(text="8")
        elif volume == 9:
            self.volume_shown.config(text="9")
        elif volume == 10:
            self.volume_shown.config(text="10")

    def volumedown(self)-> None:
        """
        turns the volume down and shows the volume on the volume_shown label

        """
        tv_1.volume_down()
        volume=tv_1.get_volume()
        self.mute_shown.config(text="UNMUTED")
        if volume == 0:
            self.volume_shown.config(text="0")
        elif volume==1:
            self.volume_shown.config(text="1")
        elif volume == 2:
            self.volume_shown.config(text="2")
        elif volume == 3:
            self.volume_shown.config(text="3")
        elif volume == 4:
            self.volume_shown.config(text="4")
        elif volume == 5:
            self.volume_shown.config(text="5")
        elif volume == 6:
            self.volume_shown.config(text="6")
        elif volume == 7:
            self.volume_shown.config(text="7")
        elif volume == 8:
            self.volume_shown.config(text="8")
        elif volume == 9:
            self.volume_shown.config(text="9")
        elif volume == 10:
            self.volume_shown.config(text="10")


    def channelup(self)->None:
        """
        turns the channel to the next channel
        """
        tv_1.channel_up()
        channel=tv_1.get_channel()
        if channel ==0:
            self.channel.config(text="Channel 0")
            self.channel_name.config(text="NONE")
        elif channel ==1:
            self.channel.config(text="Channel 1")
            self.channel_name.config(text="CNN")
        elif channel == 2:
            self.channel.config(text="Channel 2")
            self.channel_name.config(text="BBC")
        elif channel == 3:
            self.channel.config(text="Channel 3")
            self.channel_name.config(text="NBC")
        elif channel == 4:
            self.channel.config(text="Channel 4")
            self.channel_name.config(text="Cartoon Network")
        elif channel == 5:
            self.channel.config(text="Channel 5")
            self.channel_name.config(text="Nickelodeon")
    def channeldown(self)->None:
        """
        turns the channel to the previous channel
        """
        tv_1.channel_down()
        channel=tv_1.get_channel()
        if channel == 0:
            self.channel.config(text="Channel 0")
            self.channel_name.config(text="NONE")
        elif channel == 1:
            self.channel.config(text="Channel 1")
            self.channel_name.config(text="CNN")
        elif channel == 2:
            self.channel.config(text="Channel 2")
            self.channel_name.config(text="BBC")
        elif channel == 3:
            self.channel.config(text="Channel 3")
            self.channel_name.config(text="NBC")
        elif channel == 4:
            self.channel.config(text="Channel 4")
            self.channel_name.config(text="Cartoon Network")
        elif channel == 5:
            self.channel.config(text="Channel 5")
            self.channel_name.config(text="Nickelodeon")
    def mute(self)->None:
        """
        mutes the tv, which brings the volume to 0
        """
        if tv_1.get_muted()== False:
            tv_1.mute()
            self.mute_shown.config(text="MUTED")
            self.volume_shown.config(text="0")
        elif tv_1.get_muted()==True:
            tv_1.mute()
            self.mute_shown.config(text="UNMUTED")
            self.volume_shown.config(text=tv_1.get_volume_stored())
