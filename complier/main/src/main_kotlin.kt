import org.antlr.runtime.tree.ParseTree
import org.antlr.v4.runtime.CharStream
import org.antlr.v4.runtime.CharStreams
import org.antlr.v4.runtime.CommonTokenStream

import java.io.IOException

object main {
    @Throws(IOException::class)
    @JvmStatic
    fun main(args: Array<String>) {
        val charStream = CharStreams.fromFileName("./test.cpp")
        val cpp14Lexer = CPP14Lexer(charStream)
        val commonTokenStream = CommonTokenStream(cpp14Lexer)
        val cpp14Parser = CPP14Parser(commonTokenStream)

        val parseTree = cpp14Parser.translationunit()


        println("Done")
    }
}
