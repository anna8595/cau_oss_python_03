"""
figure 모듈은 함수 및 클래스로 이러어진 모듈입니다. 
line class로 선의 길이 설정 및 참조를 수행하며 
area_square, area_circle, area_regular_triangle 함수로 
각각 정사각형, 원, 정삼각형의 넓이를 반환합니다. 

"""
import math

class line:
    """
    line class는 선의 길이에 대한 정보를 저장하는 클래스입니다. 
    외부에서 접근 불가능한 변수 __length가 있으며, 
    이 변수를 수정하고 접근하기 위해 set_length와 get_length 메소드가 포함되어 있습니다. 
    """
    __length = 0
    def __init__(self, length):
        """생성자 초기 length 값을 받기
        Args:
            length (int or float): 초기 선의 길이 값
        """
        self.__length = length

    def set_length(self, length):
        """선의 길이를 수정
        Args:
            length (int or float): 수정하고자 하는 선의 길이 값 
        """
        self.__length = length
    
    def get_length(self):
        """객체가 저장하고 있는 선의 길이를 반환 
        Returns:
            int or float: 저장하고 있는 선의 길이
        """
        return self.__length

def area_square(length):
    """길이를 입력받아 정사각형의 넓이를 구하는 함수
    Args:
        length (int or float): 한변의 길이 
    Returns:
        int or float: 정사각형의 넓이 반환
    """
    return length * length

def area_circle(length):
    """길이를 입력받아 원의 넓이를 구하는 함수
    Args:
        length (int or float): 반지름의 길이 
    Returns:
        int or float: 원의 넓이 반환
    """
    return length * length * math.pi

def area_regular_triangle(length):
    """길이를 입력받아 정삼각형의 넓이를 구하는 함수
    Args:
        length (int or float): 한변의 길이 
    Returns:
        int or float: 정삼각형의 넓이 반환
    """
    return length * length * math.sqrt(3) / 4
