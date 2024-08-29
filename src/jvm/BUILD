java_sources(name="jlib")

kotlin_sources(name="klib")

scala_sources(
    name="slib",
    scalac_plugins=["semanticdb"],
)

jvm_artifact(
    name="org.scala-lang_scala-library_2.13.6",
    group="org.scala-lang",
    artifact="scala-library",
    version="2.13.6",
)

jvm_artifact(
    name="org.jetbrains.kotlin_kotlin-reflect",
    group="org.jetbrains.kotlin",
    artifact="kotlin-reflect",
    version="1.6.20",
)

jvm_artifact(
    name="org.jetbrains.kotlin_kotlin-script-runtime",
    group="org.jetbrains.kotlin",
    artifact="kotlin-script-runtime",
    version="1.6.20",
)

jvm_artifact(
    name="org.jetbrains.kotlin_kotlin-stdlib",
    group="org.jetbrains.kotlin",
    artifact="kotlin-stdlib",
    version="1.6.20",
)

scala_artifact(
    name="semanticdb-jar",
    group="org.scalameta",
    artifact="semanticdb-scalac",
    version="4.8.4",
    crossversion="full",
)

scalac_plugin(name="semanticdb", artifact=":semanticdb-jar")
