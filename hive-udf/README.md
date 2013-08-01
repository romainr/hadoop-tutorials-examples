Blog URL
========
Coming soon

```
git clone https://github.com/romainr/hadoop-tutorials-examples.git
cd hive-udf
```

- Just use [myudf.jar](myudf.jar)

- Or compile it with:
```
javac -cp $(ls /usr/lib/hive/lib/hive-exec*.jar):/usr/lib/hadoop/hadoop-common.jar org/hue/udf/MyUpper.java
jar -cf myudfs.jar  -C . .
```
