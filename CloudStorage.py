from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
    
def main():
    access_token='eB-3UKUtV98AAAAAAAAAASNRdWkcDRMUoAHqkj-A1jGImBUJPkRMCqd3cpbTjWWE'
    transferData=TransferData(access_token)
    file_from=input('Enter the file path to transfer: ')
    file_to=input('Enter the full part to upload to dropbox')
    transferData.upload_file(file_from,file_to)
    print('The file has been moved')

main()