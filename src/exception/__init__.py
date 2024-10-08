import os,sys

class CustomException(Exception):
    def __init__(self,error_message:Exception,error_details:sys):
        self.error_message=CustomException.get_detailed_error_message(error_message=error_message,error_details=error_details)


    @staticmethod
    def get_detailed_error_message(error_message:Exception,error_details:sys)->str:
        _,_,exec_tb=error_details.exc_info()

        exception_block_line_no=exec_tb.tb_frame.f_lineno
        try_block_line_no=exec_tb.tb_lineno
        file_name=exec_tb.tb_frame.f_code.co_filename


        error_message=f"""
         Error occure in exection of:
         [{file_name}] at
         try block line no:[{try_block_line_no}]
         and exception block line no:[{exception_block_line_no}]
         error message:[{error_message}]

         
        """

        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__