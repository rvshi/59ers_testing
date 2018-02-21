import logging
from logging_config import config


class BadNumbersException(Exception):
    pass


class ListOps:
    """Class to perform several basic operations on lists of integers.
    """

    def __init__(self, l):
        """Inits the list object for internal storage.
        
        :param l: list of integers to perform operations on
        """
        # init logging config
        logging.basicConfig(**config)
        self.logger = logging.getLogger(__name__)

        self.__list = None
        self.list = l
        self.np = self.import_modules()  # import numpy

    @property
    def list(self):
        """List object for class
        """

        return self.__list

    @list.setter
    def list(self, list):
        """Updates the value of self.__list while checking inputs.
        
        See self.check_inputs(l) for exceptions raised
        :param list: list object to input
        """
        self.check_inputs(list)
        self.__list = list

    def get_sum(self):
        """ Returns the sum of a list

        :returns: sum of all the n integers in the list
        """
        self.logger.info('Calculating sum of the list')
        self.logger.debug('Input list: %s', str(self.list))
        self.logger.debug('Output: %s', sum(self.list))
        return sum(self.list)

    def get_min_max(self):
        """ Returns min and max in a list

        :returns: min and max of list in a tuple
        """
        min_max = (self.np.amin(self.list),
                   self.np.amax(self.list))

        self.logger.info('Obtaining min and max of list')
        self.logger.debug('Input list: %s', str(self.list))
        self.logger.debug('Output: %s', str(min_max))
        return min_max

    def get_max_diff(self):
        """ Returns maximum difference between consecutive elements in input list

        :returns: maximum difference d defined by d = self.list[i+1] - self.list[i] for i = 0 to n-1
        """
        diff_arr = self.np.diff(self.list)
        max_diff = self.np.max(diff_arr)
        
        self.logger.info('Calculating maximum difference in the list')
        self.logger.debug('Input list: %s', str(self.list))
        self.logger.debug('Output: %s', str(max_diff))
        return max_diff

    def import_modules(self):
        """ Imports required module (Numpy)

        :returns: the module Numpy
        """
        try:
            import numpy as np
        except (ModuleNotFoundError, ImportError) as error:
            raise ImportError(
                '''Could not import numpy. Please make sure to have the package installed''')
        self.logger.info('Imported numpy module')
        return np

    def check_inputs(self, l):
        """ Checks if input list fits desired format
        
        :param l: list of n integers between -9,000 and 9,000
        :raises TypeError: Input must be lists
        :raises TypeError: Input elements must be integers
        :raises ValueError: All input elements must be between -9,000 and 9,000 (inclusive)
        :raises BadNumbersException: Numbers 123 and 321 cannot be in same list
        """
        if(not type(l) is list):
            raise TypeError('Input must be a list')

        if(not all([type(num) is int for num in l])):
            self.logger.error("TypeError in setting list: must be list of integers")
            raise TypeError('All inputs in list must be integers.')

        if(any([abs(num) > 9000 for num in l])):
            self.logger.error(
                "ValueError in setting list: integers must be between -9,000 and 9,000")
            raise ValueError('All inputs must be between -9,000 and 9,000 (inclusive)')
        elif (any([abs(num) > 8500 for num in l])):
            self.logger.warning('Some of your inputs are very close to 9000. Be careful to not exceed 9000!')
        elif (any([abs(num) > 7000 for num in l])):
            self.logger.warning('Some of your inputs are somewhat close to 9000. Be careful to not exceed 9000!')

        if(123 in l and 321 in l):
            raise BadNumbersException('List cannot contain both 123 and 321')
