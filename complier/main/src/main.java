import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;

import java.io.IOException;

public class main {
    public static void main(String[] args) throws IOException{

        CharStream charStream = CharStreams.fromFileName("./test.swift");
        Swift3Lexer swift3Lexer = new Swift3Lexer(charStream);
        CommonTokenStream commonTokenStream = new CommonTokenStream(swift3Lexer);
        Swift3Parser swift3Parser = new Swift3Parser(commonTokenStream);

        swift3Parser.control_transfer_statement();

        System.out.println("Done");
    }
}
