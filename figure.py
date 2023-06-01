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
    __width = 0
    __height = 0
    def __init__(self, width, height):
        """생성자 초기 width 와 height 값을 받기
        Args:
            width (int or float): 초기 선의 가로 길이 값
            height (int or float): 초기 선의 세로 길이 값
        """
        self.__width = width
        self.__height = height

    def set_length(self, width, height):
        """선의 길이를 수정
        Args:
            width (int or float): 수정하고자 하는 선의 가로 길이 값 
            height (int or float): 수정하고자 하는 선의 세로 길이 값 
        """
        self.__width = width
        self.__height = height
    
    def get_length(self):
        """객체가 저장하고 있는 선의 길이를 반환 
        Returns:
            int or float: 저장하고 있는 선의 길이
        """
        return self.__width, self.__height

def area_rectangle(width, height):
    """길이를 입력받아 직사각형의 넓이를 구하는 함수
    Args:
        width (int or float): 밑변의 길이 
        height (int or float): 높이의 길이
    Returns:
        int or float: 직사각형의 넓이 반환
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height

def area_ellipse(width, height):
    """길이를 입력받아 타원의 넓이를 구하는 함수
    Args:
        width (int or float): 짧은 쪽 반지름의 길이
        height (int or float): 긴 쪽 반지름의 길이 
    Returns:
        int or float: 타원의 넓이 반환
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi

def area_right_triangle(width, height):
    """길이를 입력받아 직삼각형의 넓이를 구하는 함수
    Args:
        width (int or float): 밑변의 길이
        height (int or float): 높이의 길이 
    Returns:
        int or float: 직삼각형의 넓이 반환
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2
