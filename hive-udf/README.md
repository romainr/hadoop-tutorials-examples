How to
======

- Just use the precompiled [myudfs.jar](myudfs.jar)

- Or compile it with:
```
javac -cp $(ls /usr/lib/hive/lib/hive-exec*.jar):/usr/lib/hadoop/hadoop-common.jar org/hue/udf/MyUpper.java
jar -cf myudfs.jar  -C . .
```
