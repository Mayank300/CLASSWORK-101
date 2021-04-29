import dropbox


class TransferData(object):
    def __init__(self, acces_token):
        self.acces_token = acces_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.acces_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        


def main():
    acces_token = "sl.AveDyPM4jNDxcR8lLr3ubijvdhV4vbRcO5Ragk32GL6kvah947ILrcMGyKfZsys1T6wtOwYqFv_QS2A0GIXDD4tgHeXhRy0KdydFsPqibqqP6bTkhTMEPfoyLmNZLkjNMkBxc6w"
    transferData = TransferData((acces_token))

    file_from = input("name of the file path : ")
    file_to = input("enter the full path of the file to upload to dropbox : ")

    transferData.upload_files(file_from, file_to)

    print("file uploaded successfully =)")


# if __name__ == "__main__":
main()
