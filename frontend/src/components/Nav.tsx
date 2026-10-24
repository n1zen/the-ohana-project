import { NavLink } from "react-router";

type NavBarLink = { label: string; to: string };

const links: NavBarLink[] = [
  { label: "Home", to: "/" },
  { label: "About", to: "/about" },
];

function Nav() {
  return (
    <nav>
      <ul>
        {links.map((link) => (
          <li key={link.to}>
            <NavLink
              to={link.to}
              end={link.to === "/"}
              className={({ isActive }) => (isActive ? "active-classes" : "inactive-classes")}
            >
              {link.label}
            </NavLink>
          </li>
        ))}
      </ul>
    </nav>
  );
}

export default Nav;
