def extension():
    fileName = input("File name: ").lower().strip()
    if "." in fileName:
        file, extension = fileName.rsplit(".", maxsplit=1)
        match extension:
            case "gif":
                print("image/gif")
            case "jpg" | "jpeg":
                print("image/jpeg")
            case"png":
                print("image/png")
            case "pdf":
                print("application/pdf")
            case "txt":
                print("text/plain")
            case "zip":
                print("application/zip")
            case _ :
                print("application/octet-stream")
    else:
        print("application/octet-stream")
extension()