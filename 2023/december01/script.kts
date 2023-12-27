import java.io.File


fun readFile(name: String): List<String> {
    val text = File(name).readText()
    return text.split("\n")
}


fun findNumbers(word: String): Int {
    val numberPattern: Regex = Regex("\\d")
    val numberMatched = numberPattern.findAll(word).toList()
    val combinedString: String = numberMatched.first().value + numberMatched.last().value
    return combinedString.toInt()
}


fun partOne() {
    var total: Int = 0
    val listOfWords: List<String> = readFile("input.txt")
    for (word: String in listOfWords) total += findNumbers(word)
    println(total)
}


fun convertTextIntoNumbers(word: String): String {
    val numbersMap: Map<String, String> = mapOf("one" to "o1e", "two" to "t2o", "three" to "th3ee", "four" to "fo4r",
            "five" to "fi5e", "six" to "s6x", "seven" to "se7en", "eight" to "ei8ht", "nine" to "n9ne")
    var modifiedWord = word
    for (entry in numbersMap.entries.iterator()) modifiedWord = modifiedWord.replace(entry.key, entry.value)
    return modifiedWord
}


fun partTwo() {
    var total: Int = 0
    val listOfWords: List<String> = readFile("input.txt")
    for (word: String in listOfWords) total += findNumbers(convertTextIntoNumbers(word))
    println(total)
}


partOne()
partTwo()