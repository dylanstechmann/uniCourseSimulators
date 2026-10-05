import Markdown from "react-markdown";

export function MarkdownReader({ children }: { children: string }) {
  return (
    <div className="markdown">
      <Markdown skipHtml>{children}</Markdown>
    </div>
  );
}
