# 使用聚合工程
## 创建父工程
1. 使用https://start.spring.io/创建需要的java工程
2. 修改pom文件.添加<packaging>pom</packaging>
## 创建子工程
1. 在父工程下创建maven子工程
2. 修改打包方式为jar<packaging>jar</packaging>
3. 导入其它依赖子项目
## 使用spring-data-jpa
1. pom文件导入
# mac brew service管理service
- brew services list 
  - 查看所有存在的服务器列表
- brew services start mysql
  - 启动mysql并注册为开机自启动
- brew services stop mysql
  - 停止mysql,并取消注册开机自启动
- brew services run mysql
  - 启动mysql,不注册为开机自启动
- brew services restart mysql
  - 重启启动mysql
- brew services cleanup
  - 清理已卸载的无用程序
- 开机自启动文件存放目录
  - ~/Liberary/LaunchDaemons/