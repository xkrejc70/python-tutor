// Move styles to index.css
import React, { useState } from 'react';
import { Sidebar, SubMenu, Menu, MenuItem } from 'react-pro-sidebar';
// icons
import { RiTeamLine, RiCalendar2Line, RiUserUnfollowLine } from 'react-icons/ri';
import { FiChevronsLeft, FiChevronsRight } from 'react-icons/fi';
import { FaCode, FaUpload } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import 'assets/global.css';

function Sidebars({ onCollapsedChange }) {

  const [collapsed, setCollapsed] = useState(false);
  const [toggled, setToggled] = useState(false);

  const handleCollapsedChange = () => {
    setCollapsed(!collapsed);
    onCollapsedChange(!collapsed); // Notify the parent component about the state change
  };
  const handleToggleSidebar = (value) => {
    setToggled(value);
  };

  // TODO: move styles to .css
  return (
    <div style={{ display: "flex" }}>
      <Sidebar
        className={`app ${toggled ? "toggled" : ""}`}
        style={{ height: "100%", position: "fixed", display: "inline-block" }}
        collapsed={collapsed}
        toggled={toggled}
        handleToggleSidebar={handleToggleSidebar}
        handleCollapsedChange={handleCollapsedChange}
      >
        <main>
          <Menu>
            {collapsed ? (
              <MenuItem
                icon={<FiChevronsRight />}
                onClick={handleCollapsedChange}
              ></MenuItem>
            ) : (
              <MenuItem
                suffix={<FiChevronsLeft />}
                onClick={handleCollapsedChange}
                className="menu-item"
              >
                <div className="title">PYTHON TUTOR</div>
              </MenuItem>
            )}
            <hr />
          </Menu>

          <Menu>
            {/* Warning cuz of double <a> can use NavLink, but it breaks submenu */}
            <MenuItem icon={<FaUpload />} component={<Link to="/upload" />}>
              Upload project
            </MenuItem>
            <SubMenu defaultOpen label={"Practice"} icon={<RiTeamLine />}>
              <MenuItem icon={<FaCode />} component={<Link to="/#" />}>Regex</MenuItem>
              <MenuItem icon={<RiUserUnfollowLine />} component={<Link to="/#" />} >List</MenuItem>
              <MenuItem icon={<RiCalendar2Line />} component={<Link to="/proj8" />} >Iterable</MenuItem>
            </SubMenu>
          </Menu>

          {/* Additional Menu at the bottom outside the Sidebar */}
          <div className="menu-bottom">
            <Menu>
              <MenuItem icon={<FaUpload />} component={<Link to="/#" />}>
                smth
              </MenuItem>
            </Menu>
          </div>
        </main>
      </Sidebar>
    </div>
  );
}
export default Sidebars;
