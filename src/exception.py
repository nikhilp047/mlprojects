import sys
import logging
# whenever an exception gets raised I want to push this on my like my own custom message
def error_message_detail(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    # https://docs.python.org/3/library/sys.html
    # https://docs.python.org/3/reference/datamodel.html#traceback-objects
    error_message="Error occured in python script  [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error)) 
    return error_message 

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message  
    

if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        print("mene print kiya",e)
        raise CustomException(e,sys)
