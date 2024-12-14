class Television:
    MIN_VOLUME=0
    MAX_VOLUME=2
    MIN_CHANNEL=0
    MAX_CHANNEL= 3

    def __init__(self) -> None:
        """
        Initializes all the variable needed for the methods
        """
        self.__status= False
        self.__muted= False
        self.__volume= Television.MIN_VOLUME
        self.__channel=Television.MIN_CHANNEL
        self.__volume_stored = Television.MIN_VOLUME

    def power(self) -> None:
        """
        Turns the TV on or off
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        stores the current volume in a variable and turns the volume to zero
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
                self.__volume_stored = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__volume_stored
    def channel_up(self) -> None:
        """
        Increases the tv channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self) -> None:
        """
        Decreases the tv channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    def volume_up(self) -> None:
        """
        Increases the volume by one
        """
        if self.__status:
            self.__muted = False
            self.__volume=self.__volume_stored
            if self.__volume < Television.MAX_VOLUME:
                self.__volume +=1
        self.__volume_stored=self.__volume
    def volume_down(self) -> None:
        """
        Decreases the volume by one
        """
        if self.__status:
            self.__muted = False
            self.__volume= self.__volume_stored
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -=1
        self.__volume_stored=self.__volume
    def get_status(self)-> bool:
        """
        returns the status of the tv weather on or off

        :return: int
        """
        return self.__status

    def get_muted(self)-> bool:
        """
        returns the mute status
        :return: self.__muted
        """
        return self.__muted

    def get_volume(self) -> int:
        """
        returns the volume of the tv
        :return: returns self.__volume
        """
        return self.__volume


    def get_channel(self)-> int:
        """
        returns the

        :return: returns self.__channel
        """
        return self.__channel

    def get_volume_stored(self)-> int:
        """
        returns the volume stored before muted
        :return: returns self.__volume_stored
        """
        return self.__volume_stored
