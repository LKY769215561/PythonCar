from MyQR import myqr



myqr.run(

    # 输入链接或者句子作为参数，扫描二维码后显示
    words='https://www.jianshu.com/u/28f6cc948fa1',

    # 控制边长，范围是1到40，数字越大边长越大，默认边长是取决于你输入的信息的长度和使用的纠错等级。
    version=5,
    # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    level='H',
    # 将QR二维码图像与一张同目录下的图片相结合，此处设置该图片
    picture='640.gif',
    # 默认是黑白(False)，可以选择彩色(True)
    colorized=True,

    # 调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。
    contrast=1.0,
    # 调节图片的亮度，用法与contrast相同。
    brightness=1.0,
    # 输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif ；
    save_name='love.gif'
)