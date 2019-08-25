# 使用聚合工程
## 创建父工程
1. 使用https://start.spring.io/创建需要的java工程(选择web,test,devtool等基础项)
2. 修改pom文件.添加<packaging>pom</packaging>
## 创建子工程
1. 在父工程下创建maven子工程
2. 修改打包方式为jar<packaging>jar</packaging>
3. 导入其它依赖子项目
## 使用spring-data-jpa
1. pom文件导入spring-boot-starter-data-jpa
```
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
```
2. 配置连接池信息
```
spring:
  jpa:
    show-sql: true #是否显示sql
    hibernate:
      ddl-auto: update #自动表生成策略
  datasource:
    url: jdbc:mysql://127.0.0.1:3306/demo
    username: root
    password: root
    hikari: #使用hikari连接池
      connection-timeout: 3000
      idle-timeout: 600000
      max-lifetime: 1800000
      maximum-pool-size: 10
      pool-name: hikari
      register-mbeans: false

```
3. 创建表对应实体类,使用@Entity注解修饰实体类
4. 使用@Id,@GeneratedValue()定义主键字段确定主键生成策略
   - JPA主键生成策略的4个标准
     - TABLE 使用一个特定的数据库表格来保存主键
     - SEQUENCE：根据底层数据库的序列来生成主键，条件是数据库支持序列。(mysql不支持)
     - IDENTITY：主键由数据库自动生成（主要是自动增长型）(oracle不支持)
     - AUTO：主键由程序控制
5. 创建interface类继承JpaRepository
6. 如需使用queryDsl
    1. interface继承QuerydslPredicateExecutor
    2. POM文件添加
    ```
      <!--querydsl依赖-->
        <dependency>
            <groupId>com.querydsl</groupId>
            <artifactId>querydsl-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>com.querydsl</groupId>
            <artifactId>querydsl-apt</artifactId>
            <scope>provided</scope>
        </dependency>
        <!-- 生成Q类插件-->
        <build>
            <plugins>
                <plugin>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-maven-plugin</artifactId>
                </plugin>
                <!--添加QueryDSL插件支持-->
                <plugin>
                    <groupId>com.mysema.maven</groupId>
                    <artifactId>apt-maven-plugin</artifactId>
                    <version>1.1.3</version>
                    <executions>
                        <execution>
                            <goals>
                                <goal>process</goal>
                            </goals>
                            <configuration>
                                <outputDirectory>target/generated-sources/java</outputDirectory>
                                <processor>com.querydsl.apt.jpa.JPAAnnotationProcessor</processor>
                            </configuration>
                        </execution>
                    </executions>
                </plugin>
            </plugins>
        </build>
    ```
7. @EntityListeners(AuditingEntityListener.class) 监听新建修改时间,自动插入日期修改人
8. extends AbstractAuditable<U,Key> 自动日期类,id类
## spring-boot-starter-test
- springboot 单元测试
1. pom添加spring-boot-starter-test
```
        <dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
```
2. 添加测试类
```
//junit5
@ExtendWith(SpringExtension.class) //导入spring测试框架[2]
@SpringBootTest
@DisplayName("Test Demo")
public class TestDemo {

    @Autowired
    private SysService sysService;

    @Test
    @DisplayName("Add user")
    public void test(){
        User user = new User();
        user.setName("FromJunit");
        User newOne = sysService.save(user);
        assertAll("Insert User Success.",
                () -> assertNotNull(newOne),
                () -> assertNotNull(newOne.getId()));
    }
}
//junit4
@RunWith(SpringRunner.class)
@SpringBootTest
public class SmokeTest {

    @Autowired
    private HomeController controller;

    @Test
    public void contexLoads() throws Exception {
        assertThat(controller).isNotNull();
    }
}
//mvc test
@RunWith(SpringRunner.class)
@WebMvcTest
public class WebLayerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    public void shouldReturnDefaultMessage() throws Exception {
        this.mockMvc.perform(get("/")).andDo(print()).andExpect(status().isOk())
                .andExpect(content().string(containsString("Hello World")));
    }
}
```
3. 
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