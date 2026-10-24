interface HeaderProps {
  title: string;
}

function Header({ title }: HeaderProps) {
  return (
    <header className="py-4 pl-8 border-b border-mist-500">
      <h1 className="text-md font-semibold">{title}</h1>
    </header>
  );
}

export default Header;
