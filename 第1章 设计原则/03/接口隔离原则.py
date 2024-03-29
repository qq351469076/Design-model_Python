class 外在美:

    def 漂亮(self):
        return '漂亮'

    def 好身材(self):
        return '好身材'


class 内在美:

    def 气质(self):
        return '气质好'


class 女孩:

    def __init__(self, name_):
        self.name = name_

    def 印象(self, 外在美_, 内在美_):
        print(f'{self.name}   {外在美_.漂亮()}, {外在美_.好身材()}, {内在美_.气质()}')


if __name__ == '__main__':
    # 接口隔离原则的定义是客户端不应该依赖它不需要的接口, 类间的依赖关系应该建立在最小的接口上
    # 简单的说就是建立单一的接口, 不要建立庞大臃肿的接口, 尽量接口细化, 同时接口里面方法少, 保持接口纯洁性
    丽丽 = 女孩('丽丽')
    外在美 = 外在美()
    内在美 = 内在美()
    丽丽.印象(外在美, 内在美)
    # 这里将印象分为内在美和外在美两个接口, 系统灵活性提高了, 另外接口还能实现聚合, 系统拓展性也得到了增强

    # 接口隔离原则总结:
    #   接口尽量粒度化, 保持接口纯洁性
    #   接口要高内聚, 即减少对外的交互
