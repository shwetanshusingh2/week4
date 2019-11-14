import CloudFormation as stack
import Upload_Data as data_upload


class helper:

    def __init__(self):
        self.stacks = stack.Stack()
        self.upload_object = data_upload.Upload_Template_Python_Scripts()


    def run_all_scripts(self):
        self.upload_object.upload_all_scripts()
        self.stacks.create_upload_stack()





run_script = helper()
run_script.run_all_scripts()