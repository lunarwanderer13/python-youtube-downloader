try:
    import os
    from colored import fg, attr
except ModuleNotFoundError as err:
    print(f'{fg(1)}ModuleNotFoundError: {err}{attr(0)}')

def changeExtensionToMP3(folderPath):
    if not os.path.isdir(folderPath):
        print(f'{fg(1)}The path {folderPath} is not a valid directory.{attr(0)}')
        return

    for filename in os.listdir(folderPath):
        file_path = os.path.join(folderPath, filename)

        if os.path.isdir(file_path):
            continue

        base, ext = os.path.splitext(filename)

        newFilename = base + '.mp3'
        newFilePath = os.path.join(folderPath, newFilename)

        os.rename(file_path, newFilePath)
        print(f'{fg(69)}Renamed {fg(46)}{filename}{fg(69)} to {fg(46)}{newFilename}{fg(69)} successfully!{attr(0)}')

if __name__ == '__main__':
    folderPath = 'vids' #input(f'{fg(15)}Enter the folder path:  {attr(0)}')
    changeExtensionToMP3(folderPath)