# odootutor

几天前，我认识到odoo13 提供的脚手架自动创建产生的代码，是根本就不能在odoo13上跑起来的。那么从何处继续学习Odoo？

有人提到了，可以在Odoo免费市场上找一个现成的app，如果它不太复杂，也跑得起来，那么就可以把它当成一个脚手架代码。

我觉得言之成理，于是去Odoo Store找了不少，一个个的试用了，最后还真找到了一个比较合适的。它是一个开发者做的文档管理系统。它符合我的要求，一次就可以安装，且不太复杂。

安装的过程是：

1. 下载安装包，就是一个zip文件
2. 解压放到Odoo addon内，我的环境下，目录是“C:\Program Files (x86)\Odoo 13.0\server\odoo\addons\doc”
3. 进入Odoo界面，点击左上角的主菜单的apps子菜单，进入apps内
4. 点击菜单Update Apps List
5. 在查询框内，输入查询 document
6. 查询结果应该出现此app，点击app kanban的右上角的dropdown，展开菜单，简单菜单install
7. 主菜单内添加了一个新的菜单项：Documents， 点击Documents进入此app内

此app提供了文档管理的功能，文档可以是一个树状的，而我需要的只是一个脚手架，因此我做了不少删除和调整，包括：

1. 我删除了很多我不需要的属性，留下了name,description"等少数的属性，界面上也删掉了我不需要的。把它变成了一个极为简单的model
2. 删除了对mail的以来，
3. 删除了对sidebar的以来
4. 目前只是以来base

以及对此Model提供了最基本的CRUD功能。把它放到了我的仓库内，作为以后开发Odoo的脚手架。

在删除代码的过程中，我需要适时的看到修改代码后对app的影响，我需要更新最新的修改。做法就是：

	进入apps
	查询到此app
	点击kanban右上角的dropdown | upgrade

来升级代码。然后在进入此app，查看界面和逻辑的变化。

在修改和验证代码的过程中，我搞死过几回Odoo（出现了500 Internal Error），且重启Odoo服务，PG服务也无法解决，也遇到过Upgrade app的时候断开连接然后500 Error，也遇到过断开连接有连得上的的。

现在有一个可以用的脚手架了。我可以基于此代码块，边看文档，边编写代码验证，以实践的方式，开始对Odoo开发的学习。

原始作者叫[苏仁杰](https://renjie.me/)，看他的博客好像在腾讯工作过，居然做了十来个app，都是围绕着文档管理方向。签名也比较有趣：

	生活于、浙南山区、广东珠三角、理想移居地有、海南岛、大理城、觅志同道合者不易、且行且珍惜

猜想他可能是浙南山区人，工作于珠三角，一致寻找更好的栖居地吧。对这个人的生活状态其实有些好奇。在网络上寻找解决方案的时候，常常可以发现有趣的人，这也是网络的一个乐趣了。

