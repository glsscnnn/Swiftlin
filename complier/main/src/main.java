import org.antlr.runtime.tree.ParseTree;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;

import java.io.IOException;

public class main {
    public static void main(String[] args) throws IOException{
        CharStream charStream = CharStreams.fromFileName("./test.cpp");
        CPP14Lexer cpp14Lexer = new CPP14Lexer(charStream);
        CommonTokenStream commonTokenStream = new CommonTokenStream(cpp14Lexer);
        CPP14Parser cpp14Parser = new CPP14Parser(commonTokenStream);

        CPP14Parser.TranslationunitContext parseTree = cpp14Parser.translationunit();


        System.out.println("Done");
    }
}
