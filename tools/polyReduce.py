import os
import argparse

def main():
    """ run polyreduce outside of houdini
    """
    parser = argparse.ArgumentParser(description="find assets and polyReduce them by a given amount")
    parser.add_argument("-d", "--dir", metavar="", default="", help="a dir for find assets")
    parser.add_argument("-a", "--amount", metavar="", default="50", help="amount to reduce by")
    args = parser.parse_args()

    assetDir = args.dir
    amount = args.amount

    if not assetDir and amount:
        print("you need to supply dir and reduction amount")
        return

    command = "D:/Adobe/Houdini18.5.351/bin/"
    command += 'hython -c \"import sys; sys.path.append(\'E:/HoudiniTools/utils\');'
    command += 'import houUtils; houUtils.runReduction(\'%s\', \'%s\')\"' % (assetDir, amount)
    os.system(command)

    print("reduction complete！")


if __name__ == "__main__":
    main()
