class Television:

    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    '''This initializes the Television object with default attributes from our class variables'''

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel
        self.__prev_volume = None

    '''This method flips the boolean value of self.__status to signify off or on, False is default'''

    def power(self):
        self.__status = not self.__status
        return self.__status

    '''This method flips the boolean value of self.__mute to signify off or on, False is default'''

    def mute(self):
        if self.__status is not False and self.__muted is False:
            self.__prev_volume = self.__volume
            self.__volume = self.min_volume
            self.__muted = not self.__muted
            return self.__muted
        if self.__status is not False and self.__muted is True:
            self.__volume = self.__prev_volume
            self.__muted = not self.__muted
            return self.__muted

    '''This method checks the value of self.__channel in order to determine the correct
    channel to display. If the channel is at the maximum, then the channel will be assigned the
    minimum allowed value, in our case 0'''

    def channel_up(self):
        if self.__status is True:
            if (self.__channel >= self.min_channel or self.__channel <= 2) and self.__channel != self.max_channel:
                self.__channel += 1
            elif self.__channel == self.max_channel:
                self.__channel = self.min_channel
            return self.__channel

    '''This method checks the value of self.__channel in order to determine the correct
    channel to display. If the channel is at the minimum, then the channel will be assigned the
    maximum allowed value, in our case 3'''

    def channel_down(self):
        if self.__status is True:
            if (self.__channel <= 3 or self.__channel >= 1) and self.__channel != self.min_channel:
                self.__channel -= 1
            elif self.__channel == self.min_channel:
                self.__channel = self.max_channel
            return self.__channel

    '''This method checks the value of self.__volume in order to determine the correct
    volume to display. If the volume is at the maximum, then the value will not change.'''

    def volume_up(self):
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume == self.max_volume:
                return self.__volume
            elif self.__volume < self.max_volume:
                self.__volume += 1
                return self.__volume

    '''This method checks the value of self.__volume in order to determine the correct
    volume to display. If the volume is at the minimum, then the value will not change'''

    def volume_down(self):
        if self.__status is True:
            if self.__muted is True:
                self.__muted = False
                self.__volume = self.__prev_volume
            if self.__volume == self.min_volume:
                return self.__volume
            elif self.__volume > self.min_volume:
                self.__volume -= 1
                return self.__volume

    '''This method gives logic to the print statements from this class, I think'''
    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'




